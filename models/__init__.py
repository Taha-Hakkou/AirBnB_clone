#!/usr/bin/env python3
"""
__init__.py
"""
from .engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
