---
title: "Stable gene expression for normalisation and single-sample scoring"
authors:
- admin
- Joseph Cursons
- Melissa J Davis
date: "2020-11-04"
doi: "https://doi.org/10.1093/nar/gkaa802"

# Schedule page publish date (NOT publication's date).
publishDate: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "Nucleic Acids Research"
publication_short: "NAR"

abstract: "Gene expression signatures have been critical in defining the molecular phenotypes of cells, tissues, and patient samples. Their most notable and widespread clinical application is stratification of breast cancer patients into molecular (PAM50) subtypes. The cost and relatively large amounts of fresh starting material required for whole-transcriptome sequencing has limited clinical application of thousands of existing gene signatures captured in repositories such as the Molecular Signature Database. We identified genes with stable expression across a range of abundances, and with a preserved relative ordering across thousands of samples, allowing signature scoring and supporting general data normalisation for transcriptomic data. Our new method, stingscore, quantifies and summarises relative expression levels of signature genes from individual samples through the inclusion of these ‘stably-expressed genes’. We show that our list of stable genes has better stability across cancer and normal tissue data than previously proposed gene sets. Additionally, we show that signature scores computed from targeted transcript measurements using stingscore can predict docetaxel response in breast cancer patients. This new approach to gene expression signature analysis will facilitate the development of panel-type tests for gene expression signatures, thus supporting clinical translation of the powerful insights gained from cancer transcriptomic studies."

# Summary. An optional shortened abstract.
summary: This work proposes an extension to our robust single-sample molecular phenotyping method, singscore, that works on targeted transcriptomic panels with as few as 5 endogenous control genes, thus taking the approach a step closer to the clinic.

tags:
- gene-set enrichment analysis
- molecular phenotypes
- stably expressed genes
- endogenous control RNA
- breast cancer
featured: false

links:
- name: Bioconductor
  url: https://www.bioconductor.org/packages/release/bioc/html/singscore.html
- name: Workshop
  url: https://davislaboratory.github.io/GenesetAnalysisWorkflow/
url_pdf: 'https://academic.oup.com/nar/article-pdf/48/19/e113/34133573/gkaa802.pdf'
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
  caption: 'Schematic of stingscore (singscore with stably expressed genes)'
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
