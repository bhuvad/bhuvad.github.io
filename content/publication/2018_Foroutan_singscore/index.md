---
title: "Single sample scoring of molecular phenotypes"
authors:
- Momeneh Foroutan
- admin
- Ruqian Lyu
- Kristy Horan
- Joseph Cursons
- Melissa J Davis
date: "2018-11-06"
doi: "https://doi.org/10.1186/s12859-018-2435-4"

author_notes:
  - 'Co-first author'
  - 'Co-first author'

# Schedule page publish date (NOT publication's date).
publishDate: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "BMC Bioinformatics"
publication_short: "BMC Bioinform"

abstract: "Background: Gene set scoring provides a useful approach for quantifying concordance between sample transcriptomes and selected molecular signatures. Most methods use information from all samples to score an individual sample, leading to unstable scores in small data sets and introducing biases from sample composition (e.g. varying numbers of samples for different cancer subtypes). To address these issues, we have developed a truly single sample scoring method, and associated R/Bioconductor package singscore (https://bioconductor.org/packages/singscore).

Results: We use multiple cancer data sets to compare singscore against widely-used methods, including GSVA, z-score, PLAGE, and ssGSEA. Our approach does not depend upon background samples and scores are thus stable regardless of the composition and number of samples being scored. In contrast, scores obtained by GSVA, z-score, PLAGE and ssGSEA can be unstable when less data are available (NS<25). The singscore method performs as well as the best performing methods in terms of power, recall, false positive rate and computational time, and provides consistently high and balanced performance across all these criteria. To enhance the impact and utility of our method, we have also included a set of functions implementing visual analysis and diagnostics to support the exploration of molecular phenotypes in single samples and across populations of data.

Conclusions: The singscore method described here functions independent of sample composition in gene expression data and thus it provides stable scores, which are particularly useful for small data sets or data integration. Singscore performs well across all performance criteria, and includes a suite of powerful visualization functions to assist in the interpretation of results. This method performs as well as or better than other scoring approaches in terms of its power to distinguish samples with distinct biology and its ability to call true differential gene sets between two conditions. These scores can be used for dimensional reduction of transcriptomic data and the phenotypic landscapes obtained by scoring samples against multiple molecular signatures may provide insights for sample stratification."

# Summary. An optional shortened abstract.
summary: singscore is a robust rank-based method to compute molecular phenotypes scores for individual samples such as those originating from an individual patient in the clinic

tags:
- gene-set enrichment analysis
- molecular phenotypes
- breast cancer
- EMT
featured: true

links:
- name: Bioconductor
  url: https://www.bioconductor.org/packages/release/bioc/html/singscore.html
- name: Workshop
  url: https://bioconductor.org/packages/release/workflows/html/SingscoreAMLMutations.html
url_pdf: 'https://bmcbioinformatics.biomedcentral.com/counter/pdf/10.1186/s12859-018-2435-4.pdf'
url_code: 'https://github.com/DavisLaboratory/singscore'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: 'https://www.youtube.com/watch?v=pyHG9Qww-xk'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Schematic of singscore'
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
