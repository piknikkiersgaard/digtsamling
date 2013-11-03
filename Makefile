
pdf:	index.rst
	rst2pdf index.rst

index.rst:
	find . -type f \( -iname "*.rst" ! -iname "index.rst" \) -exec echo ".. include::" {} \; > index.rst

clean:
	rm *.rst~

