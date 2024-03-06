import pytest

from dtprecommit_hooks.check_email_domain import main
from dtprecommit_hooks.utils import cmd_output


@pytest.fixture
def temp_git_dir(tmpdir):
    git_dir = tmpdir.join('gits')
    cmd_output('git', 'init', '--', str(git_dir))
    yield git_dir

def test_wrong_email_domain(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'config', '--local', 'user.email', 'email@rightdomain.com')
        assert main(["wrongdomain.com", "other.wrongdomain.com"]) == 1

def test_right_email_domain(temp_git_dir):
    with temp_git_dir.as_cwd():
        cmd_output('git', 'config', '--local', 'user.email', 'email@other.rightdomain.com')
        assert main(["rightdomain.com", "other.rightdomain.com"]) == 0
        cmd_output('git', 'config', '--local', 'user.email', 'email@rightdomain.com')
        assert main(["rightdomain.com"]) == 0
