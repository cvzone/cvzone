from distutils.core import setup

setup(
    name='cvzone',
    packages=['cvzone'],
    version='0.4',
    license='MIT',
    description='Computer Vision Helping Library',
    author='Computer Vision Zone',
    author_email='contact@computervision.zone',
    url='https://github.com/user/reponame',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords=['ComputerVision', 'HandTracking', 'FaceTracking', 'PoseEstimation'],
    install_requires=[
        'opencv-python',
        'mediapipe',
        'numpy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
