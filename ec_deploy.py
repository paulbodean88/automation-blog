from json import load
from subprocess import Popen, PIPE
from time import sleep


class SSHClient(object):

    def __init__(self, user, host_address):
        self.__user = user
        self.__host_address = host_address
        self._connection = None

    def connect_with_certificate(self, path_to_certificate):
        arguments = ['ssh', '-i', path_to_certificate, self.__user + '@' + self.__host_address]
        self._connection = Popen(arguments, stdin=PIPE)
        
    def cd(self, path):
        self._connection.stdin.write(bytes('cd ' + path + '\n', encoding='utf-8'))
        
    def hard_reset(self):
        self._connection.stdin.write(bytes('git reset --hard\n', encoding='utf-8'))
        
    def update(self, branch):
        self._connection.stdin.write(bytes('git fetch\n', encoding='utf-8'))
        self._connection.stdin.write(bytes('git checkout ' + branch + '\n', encoding='utf-8'))
        self._connection.stdin.write(bytes('git pull\n', encoding='utf-8'))

    def execute(self):
        self._connection.communicate()


class SSHDeploy(SSHClient):
    def __init__(self, user, host_address):
        super().__init__(user, host_address)
        
    def deploy(self, config):
        self.cd(config['project-root'])
        self.update(config['deploy-branch'])
        self.cd('../..')
        self._connection.stdin.write(bytes('sudo venvs/automation-blog/bin/python apps/automation-blog/automation_blog/manage.py runserver ' + config['deploy-on'] + '\n', encoding='utf-8'))
        self.execute()


if __name__ == '__main__':
    proj_config = load(open('../project.config', 'r'))
    remote = SSHDeploy(proj_config['username'], proj_config['host-server'])
    remote.deploy(proj_config)
