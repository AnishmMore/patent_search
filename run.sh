#!/bin/bash

# Check if all dependencies are installed
if python3 -c "import pkg_resources; \
    all(pkg_resources.get_distribution(dist).version in line \
        for line in open('requirements.txt') \
        for dist in line.split('=')[0].strip())";
then
    # Dependencies are already installed
    echo "All dependencies are already installed."
else
    # Some dependencies are missing, so install them
    echo "Installing missing dependencies..."
    pip install --ignore-installed -r requirements.txt
    echo "Dependencies installed."
fi

# Run app
python3 app.py