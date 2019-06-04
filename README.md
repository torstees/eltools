# eltools
Edwards Lab Tools

Just some scripts and supporting functions requested by various lab members

## Tools
Some basic tools requested by various lab members.

### mxcovar
Process VCF file(s) and build covariance matrices ready for use with MetaXcan

(this script is a work in progress and probably won't work for anything but the
task it was specifically designed for. However, I'll work to make it suitable
for more general applications in the near future)

### pseudo_parallel
Launch and maintain N processes simultaneously on a single node. This is helpful if you
have a number of tasks that need to be run but you don't want to submit them to
the cluster.

Add a single (executable) line for each "job" to a text file and pass it to the script
