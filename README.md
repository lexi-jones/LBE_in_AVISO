# LBE_in_AVISO
Identifying the semi-permanent Lofoten Basin Eddy (LBE) in the AVISO META3.2 DT eddy atlas (https://www.aviso.altimetry.fr/en/data/products/value-added-products/global-mesoscale-eddy-trajectory-product/meta3-2-dt.html). 

Using the allsat long track (10+ days) dataset. I also tested the twosat dataset but it had more breaks in the LBE compared to allsat. There were no short tracks (<10 days) in the LBE location. 

1. Tracks are selected for 2010 - 2022 and eddy centers within the Lat bounds: 69.3 - 70.2 and Lon bounds: 1.5 – 5.
2. Small eddy merges and splits are removed from the dataset.
3. The following track IDs are extracted to create an LBE-specfic dataset: [417635, 504597, 542646, 548225, 586453, 598992, 667049, 756724]

'play_w_LBE_AVISO_data.ipynb' is a Jupyter Notebook created to get started with the dataset.

