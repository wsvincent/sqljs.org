from fabric.api import local, task, cd, run


@task
def serve():
    local('python3 -m http.server')


@task
def deploy():
    local('git push origin master')
    local('s3_website push')
