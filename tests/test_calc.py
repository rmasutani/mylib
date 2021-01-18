import click
import pytest
from click.testing import CliRunner

from mylib.calc import add, mul

def test_add():
    
