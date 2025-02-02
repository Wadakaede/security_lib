from setuptools import setup, find_packages # type: ignore

setup(
    name="security_lib",  # パッケージ名
    version="1.0.0",  # バージョン
    description="A custom security library with hashing, encryption, and network tools",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/security_lib",  # リポジトリがあれば
    packages=find_packages(),  # パッケージ自動検出
    install_requires=[
        "cryptography>=3.4.8"  # 必要な依存ライブラリ
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
