#https://gist.github.com/temoto/ac4088528bc99c768468
FROM ubuntu:16.04

# inspired by https://github.com/progrium/buildstep
RUN mkdir /build

#copy build script
ADD ./im_build /build
ADD ./packages.txt /build
RUN chmod --recursive go-rwx /build
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive /bin/bash /build/im_build
RUN apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


CMD ["/sbin/my_init"]

