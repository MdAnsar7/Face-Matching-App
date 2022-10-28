from setuptools import setup

setup(
    name="src",
    version="0.0.1",
    author="Md Ansar",
    description="A small Package from to whom does your face match",
    author_email="mdansar786@gmail.com",
    packages=["src"],
    python_requires=">3.7",
    install_requires=[
        'mtcnn == 0.1.0',
        'tensorflow == 2.3.1',
        'keras == 2.4.3',
        'keras-vggface == 0.6',
        'keras-applications == 1.0.8',
        'pyYAML',
        'tqdm',
        'scikit-learn',
        'streamlit',
        'bing-image-downloader'
    ],
)
