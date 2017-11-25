console.log(`
Not yet coded.
For now, manually complete these instructions:

To do this, open "node_modules/posix/src/posix.cc", and comment out these lines

    // proper order is to first chdir() and then chroot()
    if (chdir(*dir_path)) {
        return Nan::ThrowError(Nan::ErrnoException(errno, "chroot: chdir: ", ""));
    }

Then run "npm install" in its folder.
`);