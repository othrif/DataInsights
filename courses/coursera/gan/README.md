# GAN Specialization #

### Notes on downloading workspace ### 

- Click on the jupyter logo on the upper-left
- Select new terminal from the New menu
``` bash 
cd /tf
tar -czf C1W4.tar *
```
- Go back to the workspace by clicking on jupyter and download the tar file
- If your zip file is larger than 100MB, you will need to split it up into smaller files instead and download each of them, using the following commands:
``` bash 
tar -czf - ~/work | split --bytes=100MB - ~/workspaces.tar.gz
# it will create tar files: workspace.tar.gz*
```