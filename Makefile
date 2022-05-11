.PHONY: env
env:
	mamba env create -f environment.yml -p ~/envs/ligo
	bash -ic 'conda activate hw04;python -m ipykernel install --user --name ligo --display-name "IPython - ligo"


.PHONY : clean
clean :
	rm -f figures/*.png
	rm -f audio/*.wav
	rm -rf _build


.PHONY : html
html:
	jupyter-book build .
	
	
.PHONY : html-hub
html-hub:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	cd _build/html
	python -m http.server