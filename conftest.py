import sys
import os

# Add the project root directory to Python's module search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

'''
The goal of conftest.py in this project is to add the project's root directory to Python's 
module search path,
enabling correct imports of custom modules (like 'infra') 
from any test location within the project structure.
'''