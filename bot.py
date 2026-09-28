name: Run Bot and Deploy Website

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

permissions:
  contents: write

jobs:
  run-bot:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run bot script to generate HTML
        run: python bot.py

      - name: Commit and push generated index.html
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add index.html
          git diff --quiet && git diff --staged --quiet || git commit -m "Auto-update live dashboard index.html"
          git push