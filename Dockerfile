FROM winamd64/python
WORKDIR /praktyki-wp-2023-Makhintosh
COPY . /praktyki-wp-2023-Makhintosh
RUN pip install -r requirements.txt
RUN pip install pyinstaller
CMD [ "pyinstaller", "./program.py", "-F" ]