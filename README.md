# Geo Data Science Blog

A Blog about Geospatial Data Science and Algorithms created with [Quarto](https://quarto.org/) and [github pages](https://pages.github.com/).

- Created on the ashes of my blog about geospatial data science on [hashnode](https://geods.hashnode.dev/) and my [medium blog](https://medium.com/@sebastianof/), as well as the defunct [https://geospatial.netlify.app/](https://geospatial.netlify.app/) blog deployed on netlify.
- To start reading the blog hosted on github pages, please go to <https://sebastianof.github.io/GeoDsBlog/>
- To know more about the blog, go to the [about](https://sebastianof.github.io/GeoDsBlog/about/about.html) page.

## Blog local development

- To render the website with latest changes:

```bash
make render
```

- To view the results in local:

```bash
make open
```

- To deploy to <https://sebastianof.github.io/GeoDsBlog/> simply push branch and merge.

## Create the python environment

The python environment is managed with [uv](https://docs.astral.sh/uv/guides/install-python/):

```bash
uv venv --python 3.12.4
source .venv/bin/activate
uv pip install -r <blog post folder path>/requirements.txt
```

To activate the virtualenvironment created with `uv` run:


```bash
source .venv/bin/activate
```

## License

This blog is licensed under [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/)

## Acknowledgements

The following data scientist, colleagues, professionals and friends have contributed to this blog with direct feedback or with indirect inspirations.
The author is the sole responsible for bugs, writing styles and occasional opinions.

- [Abdishakur](https://medium.com/@shakasom)
- [Albert Rapp](https://albert-rapp.de/posts/13_quarto_blog_writing_guide/13_quarto_blog_writing_guide.html)
- [Bea Milz](https://beamilz.com/posts/2022-06-05-creating-a-blog-with-quarto/en/)
- [Herbert Lui](https://herbertlui.medium.com/)
- [Khuyen Tran](https://khuyentran1476.medium.com/)
- [Maciej Tarsa](https://medium.com/@maciejtarsa)
- [Maxime Labonne](https://mlabonne.github.io/blog/)
- [Qiusheng Wu](https://github.com/giswqs)
