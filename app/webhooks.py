import hmac
from flask import Flask, request, Blueprint, jsonify, current_app 
from git import Repo

webhook = Blueprint('webhook', __name__, url_prefix='')
app = Flask(__name__)

@webhook.route('/api/netbox', methods=['POST']) 
def handle_github_hook(): 
  """ Entry point for github webhook """

  signature = request.headers.get('X-Hub-Signature') 
  sha, signature = signature.split('=')

  secret = str.encode(current_app.config.get('GITHUB_SECRET'))

  hashhex = hmac.new(secret, request.data, digestmod='sha1').hexdigest()
  if hmac.compare_digest(hashhex, signature): 
    repo = Repo(current_app.config.get('REPO_PATH')) 
    origin = repo.remotes.origin 
    origin.pull('--rebase')

    commit = request.json['after'][0:6]
    print('Repository updated with commit {}'.format(commit))
  return jsonify({}), 200

# main entry
if __name__ == '__main__':
    # run app when script is been execute
    # this will create a web server at port 8080, you can visit http://0.0.0.0:8080/
    app.run(host='0.0.0.0', port=5000, debug=True)