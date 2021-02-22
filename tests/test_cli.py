from click.testing import CliRunner
from modelindex.commands.cli import cli


def test_cli_invocation():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0


def test_cli_check_ok():
    runner = CliRunner()
    result = runner.invoke(cli, ["check", "tests/test-mi/11_markdown/rexnet.md"])
    assert result.exit_code == 0
    assert "Checking" in result.output
    assert "All good" in result.output


def test_cli_check_fail():
    runner = CliRunner()
    result = runner.invoke(cli, ["check", "tests/test-mi/01_base"])
    assert result.exit_code == 0
    assert "Path to README file docs/inception-v3-readme.md is not a valid file" in result.output
