
pdf:	index.rst
	rst2pdf index.rst

index.rst:
	echo ".. include:: forside.rst" > index.rst
	find . -type f \( -iname "*.rst" ! -iname "index.rst" ! -iname "forside.rst" \) -exec echo ".. include::" {} \; >> index.rst

clean:
	rm index.rst index.pdf *.rst~

