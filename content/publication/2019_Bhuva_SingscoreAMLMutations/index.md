---
title: "Using singscore to predict mutation status in acute myeloid leukemia from transcriptomic signatures"
authors:
- admin
- Momeneh Foroutan
- Yi Xie
- Ruqian Lyu
- Joseph Cursons
- Melissa J Davis
date: "2019-10-14"
doi: "https://doi.org/10.12688/f1000research.19236.3"

# Schedule page publish date (NOT publication's date).
publishDate: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "F1000Research"
publication_short: ""

abstract: "Advances in RNA sequencing (RNA-seq) technologies that measure the transcriptome of biological samples have revolutionised our ability to understand transcriptional regulatory programs that underpin diseases such as cancer. We recently published singscore - a single sample, rank-based gene set scoring method which quantifies how concordant the transcriptional profile of individual samples are relative to specific gene sets of interest. Here we demonstrate the application of singscore to investigate transcriptional profiles associated with specific mutations or genetic lesions in acute myeloid leukemia. Using matched genomic and transcriptomic data available through the TCGA we show that scoring of appropriate signatures can distinguish samples with corresponding mutations, reflecting the ability of these mutations to drive aberrant transcriptional programs involved in leukemogenesis. We believe the singscore method is particularly useful for studying heterogeneity within a specific subsets of cancers, and as demonstrated, we show the ability of singscore to identify where alternative mutations appear to drive similar transcriptional programs."

# Summary. An optional shortened abstract.
summary: This workflow demonstrates the versatility of singscore by applying it to infer mutation status in cancer

tags:
- gene-set enrichment analysis
- molecular phenotypes
- predict mutation status
- AML
featured: false

links:
- name: Bioconductor
  url: https://bioconductor.org/packages/release/workflows/html/SingscoreAMLMutations.html
- name: Workshop
  url: https://bioconductor.org/packages/release/workflows/html/SingscoreAMLMutations.html
url_pdf: 'https://f1000research.com/articles/8-776/v3/pdf'
url_code: 'https://github.com/DavisLaboratory/singscore'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'singscore is able to separate patients based on their mutations status.'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
