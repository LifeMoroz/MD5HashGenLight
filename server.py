import os

from celery import states
from flask import Flask, jsonify, request
from tasks import calculate_md5_hash
from config import PORT, DOWNLOAD_PATH


# init Flask app
app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)


@app.route('/submit', methods=['POST'])
def submit():
    """ Adds a new task to the hash generation queue

    Returns:
        str: Task's id
    """
    url = request.form.get('url')
    email = request.form.get('email')
    task_id = calculate_md5_hash.delay(url, email)
    return jsonify({'id': str(task_id)}), 201


@app.route('/check', methods=['GET'])
def check():
    """ Check state of task

    Returns:
        str: result of processed task
    """

    task_id = request.args.get('id')

    if not task_id:
        return jsonify({'status': states.FAILURE, 'error': 'Bad task id'}), 404

    result = calculate_md5_hash.AsyncResult(task_id)
    if not result.ready():
        return jsonify({'status': states.STARTED})  # It may be not true, but, in general, it's ok.

    try:
        hash_value, url = result.get()
    except ValueError as e:
        return {'status': states.FAILURE, 'error': str(e)}, 400

    if result.successful():
        return jsonify({'md5': hash_value[0], 'status': states.SUCCESS, 'url': hash_value})

    return jsonify({'status': states.FAILURE, 'error': 'Unexpected error. Pls, contact administrator'}), 500


def validate_settings():
    """ Validate settings values """
    if not os.path.isdir(os.path.abspath(DOWNLOAD_PATH)):
        raise ValueError('DOWNLOAD_PATH must be valid path to existing directory')


if __name__ == '__main__':
    validate_settings()
    app.run(debug=False, port=PORT)
