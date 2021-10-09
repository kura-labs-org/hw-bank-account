FROM frostming/pdm

COPY . /app

# -- Replace with the correct path to your app's main executable
CMD ["pdm", "run", "python", "BankSession.py"]
