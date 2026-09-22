set -xe
rm blog/post_*.html || echo No posts?
python3 compile-blogs.py
