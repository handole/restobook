# RESTO Reservation

### Setup Poetry

**Pre Setup: Python 3.8.x**

1. [Install Poetry](https://python-poetry.org/docs/#installation) first on your machine,
   - Change the `virtualenvs.in-project` configuration to be installed inside the project root level instead of inside your system directory (global).
   ```
   poetry config virtualenvs.in-project true
   ```
   - More about [Poetry configuration](https://python-poetry.org/docs/configuration/)
2. Go to the project directory
3. Set Python version
   ```
   poetry env use /path/to/your/python
   ```
   - Make sure a new `.venv` folder create in the project root level
   - Run `poetry shell` to activate it via poetry, or
   - You can do it manually using `source`
4. Run `poetry install` to install package dependencies
5. Add/Remove a Package
⚠️ **Remember to add/remove ONLY the parent package** ⚠️

   - To add a package
   ```
   poetry add package-name
   ```
   - To remove a package
   ```
   poetry remove package-name
   ```

   - You can add/remove multiple packages using the respective argument.
     Example to add multiple packages:
   ```
   poetry add foo_pkg bar_pkg
   ```
6. Running apps
   ```
   poetry run python main.py
   ```