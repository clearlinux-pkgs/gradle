#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gradle
Version  : 4.3.1
Release  : 17
URL      : https://github.com/gradle/gradle/archive/v4.3.1.tar.gz
Source0  : https://github.com/gradle/gradle/archive/v4.3.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 CPL-1.0 LGPL-2.1 LGPL-2.1-only MIT
Requires: gradle-bin = %{version}-%{release}
Requires: gradle-data = %{version}-%{release}
Requires: gradle-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : buildreq-mvn
BuildRequires : ca-certs
BuildRequires : gradle
BuildRequires : mvn-GMetrics
BuildRequires : mvn-airbase
BuildRequires : mvn-airline
BuildRequires : mvn-ant
BuildRequires : mvn-ant-launcher
BuildRequires : mvn-antlr
BuildRequires : mvn-antlr4
BuildRequires : mvn-apache
BuildRequires : mvn-asciidoctor-gradle-plugin
BuildRequires : mvn-asm
BuildRequires : mvn-aws-java-sdk
BuildRequires : mvn-beanshell
BuildRequires : mvn-biz.aQute.bndlib
BuildRequires : mvn-bouncycastle
BuildRequires : mvn-cglib
BuildRequires : mvn-checkstyle
BuildRequires : mvn-codenarc
BuildRequires : mvn-commons-beanutils
BuildRequires : mvn-commons-cli
BuildRequires : mvn-commons-codec
BuildRequires : mvn-commons-collections
BuildRequires : mvn-commons-compress
BuildRequires : mvn-commons-io
BuildRequires : mvn-commons-lang
BuildRequires : mvn-commons-logging
BuildRequires : mvn-commons-math3
BuildRequires : mvn-commons-parent
BuildRequires : mvn-compiler-interface
BuildRequires : mvn-dd-plist
BuildRequires : mvn-dom4j
BuildRequires : mvn-findbugs
BuildRequires : mvn-findbugs-annotations
BuildRequires : mvn-google-api-java-client
BuildRequires : mvn-google-api-services-storage
BuildRequires : mvn-google-http-java-client
BuildRequires : mvn-groovy
BuildRequires : mvn-gson
BuildRequires : mvn-guava
BuildRequires : mvn-hamcrest
BuildRequires : mvn-http-builder
BuildRequires : mvn-httpcomponents-client
BuildRequires : mvn-httpcomponents-core
BuildRequires : mvn-incremental-compiler
BuildRequires : mvn-ivy
BuildRequires : mvn-jackson-annotations
BuildRequires : mvn-jackson-core
BuildRequires : mvn-jackson-databind
BuildRequires : mvn-jackson-parent
BuildRequires : mvn-jansi
BuildRequires : mvn-japicmp
BuildRequires : mvn-japicmp-gradle-plugin
BuildRequires : mvn-jatl
BuildRequires : mvn-javaparser-parent
BuildRequires : mvn-javassist
BuildRequires : mvn-javax.inject
BuildRequires : mvn-jcifs
BuildRequires : mvn-jcip-annotations
BuildRequires : mvn-jcommander
BuildRequires : mvn-jetbrains-annotations
BuildRequires : mvn-jhighlight
BuildRequires : mvn-jmh
BuildRequires : mvn-jmh-gradle-plugin
BuildRequires : mvn-joda-time
BuildRequires : mvn-jopt-simple
BuildRequires : mvn-jsch
BuildRequires : mvn-json-lib
BuildRequires : mvn-jsoup
BuildRequires : mvn-jsr305
BuildRequires : mvn-junit
BuildRequires : mvn-kotlin
BuildRequires : mvn-kryo
BuildRequires : mvn-maven
BuildRequires : mvn-maven-aether-provider
BuildRequires : mvn-maven-artifact
BuildRequires : mvn-maven-compat
BuildRequires : mvn-maven-core
BuildRequires : mvn-maven-model
BuildRequires : mvn-maven-model-builder
BuildRequires : mvn-maven-parent
BuildRequires : mvn-maven-plugin-api
BuildRequires : mvn-maven-repository-metadata
BuildRequires : mvn-maven-settings
BuildRequires : mvn-maven-settings-builder
BuildRequires : mvn-minlog
BuildRequires : mvn-mvnplugins
BuildRequires : mvn-native-platform
BuildRequires : mvn-nekohtml
BuildRequires : mvn-oauth-java-client
BuildRequires : mvn-objenesis
BuildRequires : mvn-oss-parents
BuildRequires : mvn-ow2
BuildRequires : mvn-parboiled
BuildRequires : mvn-pegdown
BuildRequires : mvn-plexus
BuildRequires : mvn-plexus-cipher
BuildRequires : mvn-plexus-classworlds
BuildRequires : mvn-plexus-containers
BuildRequires : mvn-plexus-interpolation
BuildRequires : mvn-plexus-utils
BuildRequires : mvn-pmaven
BuildRequires : mvn-reflectasm
BuildRequires : mvn-rhino
BuildRequires : mvn-sbt-interface
BuildRequires : mvn-scala-compiler
BuildRequires : mvn-scala-library
BuildRequires : mvn-scala-reflect
BuildRequires : mvn-simpleframework
BuildRequires : mvn-slf4j
BuildRequires : mvn-snakeyaml
BuildRequires : mvn-sonatype-aether
BuildRequires : mvn-sonatype-plexus-sec-dispatcher
BuildRequires : mvn-spock
BuildRequires : mvn-testng
BuildRequires : mvn-wagon
BuildRequires : mvn-xbean
BuildRequires : mvn-xercesImpl
BuildRequires : mvn-xml-apis
BuildRequires : mvn-xml-resolver
BuildRequires : mvn-zinc
BuildRequires : openjdk
BuildRequires : openjdk-dev
Patch1: Add-all-released-versions.patch
Patch2: Set-local-maven-repo.patch
Patch3: Enable-local-fonts.patch
Patch4: jquery.min.patch

%description
<img src="gradle.png" width="350px" alt="Gradle Logo" />
Gradle is a build tool with a focus on build automation and support for multi-language development. If you are building, testing, publishing, and deploying software on any platform, Gradle offers a flexible model that can support the entire development lifecycle from compiling and packaging code to publishing web sites. Gradle has been designed to support build automation across multiple languages and platforms including Java, Scala, Android, C/C++, and Groovy, and is closely integrated with development tools and continuous integration servers including Eclipse, IntelliJ, and Jenkins.

%package bin
Summary: bin components for the gradle package.
Group: Binaries
Requires: gradle-data = %{version}-%{release}
Requires: gradle-license = %{version}-%{release}

%description bin
bin components for the gradle package.


%package data
Summary: data components for the gradle package.
Group: Data

%description data
data components for the gradle package.


%package license
Summary: license components for the gradle package.
Group: Default

%description license
license components for the gradle package.


%prep
%setup -q -n gradle-4.3.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
## build_prepend content
mkdir -p build/
cp all-released-versions.json build/
mkdir -p /builddir/.m2/repository/jquery/jquery.min/1.11.0
cp jquery.min.js /builddir/.m2/repository/jquery/jquery.min/1.11.0/jquery.min-1.11.0.js
export LC_ALL=en_US.UTF-8
export LC_MESSAGES="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
mkdir -p /builddir/.m2
cp -r /usr/share/java/.m2/* /builddir/.m2/
gradle --offline -Pgradle_installPath=/tmp/gradle -PfinalRelease=true install --exclude-task \
:docs:configureCss

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gradle
cp LICENSE %{buildroot}/usr/share/package-licenses/gradle/LICENSE
cp subprojects/distributions/src/toplevel/NOTICE %{buildroot}/usr/share/package-licenses/gradle/subprojects_distributions_src_toplevel_NOTICE
cp subprojects/docs/src/docs/userguide/licenses.adoc %{buildroot}/usr/share/package-licenses/gradle/subprojects_docs_src_docs_userguide_licenses.adoc
cp subprojects/docs/src/samples/application/src/dist/LICENSE %{buildroot}/usr/share/package-licenses/gradle/subprojects_docs_src_samples_application_src_dist_LICENSE
cp subprojects/docs/src/samples/play/custom-assets/copyright.txt %{buildroot}/usr/share/package-licenses/gradle/subprojects_docs_src_samples_play_custom-assets_copyright.txt
cp subprojects/docs/src/samples/play/custom-distribution/LICENSE %{buildroot}/usr/share/package-licenses/gradle/subprojects_docs_src_samples_play_custom-distribution_LICENSE
## install_append content
cp -R /tmp/gradle %{buildroot}/usr/share/
rm %{buildroot}/usr/share/gradle/bin/gradle.bat
mkdir -p %{buildroot}/usr/bin
ln -s /usr/share/gradle/bin/gradle %{buildroot}/usr/bin/gradle
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gradle

%files data
%defattr(-,root,root,-)
/usr/share/gradle/LICENSE
/usr/share/gradle/NOTICE
/usr/share/gradle/bin/gradle
/usr/share/gradle/init.d/readme.txt
/usr/share/gradle/lib/annotations-13.0.jar
/usr/share/gradle/lib/ant-1.9.6.jar
/usr/share/gradle/lib/ant-launcher-1.9.6.jar
/usr/share/gradle/lib/asm-debug-all-6.0_ALPHA.jar
/usr/share/gradle/lib/commons-collections-3.2.2.jar
/usr/share/gradle/lib/commons-compress-1.14.jar
/usr/share/gradle/lib/commons-io-2.2.jar
/usr/share/gradle/lib/commons-lang-2.6.jar
/usr/share/gradle/lib/gradle-base-services-4.3.1.jar
/usr/share/gradle/lib/gradle-base-services-groovy-4.3.1.jar
/usr/share/gradle/lib/gradle-build-cache-4.3.1.jar
/usr/share/gradle/lib/gradle-build-option-4.3.1.jar
/usr/share/gradle/lib/gradle-cli-4.3.1.jar
/usr/share/gradle/lib/gradle-core-4.3.1.jar
/usr/share/gradle/lib/gradle-core-api-4.3.1.jar
/usr/share/gradle/lib/gradle-docs-4.3.1.jar
/usr/share/gradle/lib/gradle-installation-beacon-4.3.1.jar
/usr/share/gradle/lib/gradle-jvm-services-4.3.1.jar
/usr/share/gradle/lib/gradle-kotlin-dsl-0.12.3.jar
/usr/share/gradle/lib/gradle-kotlin-dsl-tooling-builders-0.12.3.jar
/usr/share/gradle/lib/gradle-kotlin-dsl-tooling-models-0.12.3.jar
/usr/share/gradle/lib/gradle-launcher-4.3.1.jar
/usr/share/gradle/lib/gradle-logging-4.3.1.jar
/usr/share/gradle/lib/gradle-messaging-4.3.1.jar
/usr/share/gradle/lib/gradle-model-core-4.3.1.jar
/usr/share/gradle/lib/gradle-model-groovy-4.3.1.jar
/usr/share/gradle/lib/gradle-native-4.3.1.jar
/usr/share/gradle/lib/gradle-persistent-cache-4.3.1.jar
/usr/share/gradle/lib/gradle-process-services-4.3.1.jar
/usr/share/gradle/lib/gradle-resources-4.3.1.jar
/usr/share/gradle/lib/gradle-runtime-api-info-4.3.1.jar
/usr/share/gradle/lib/gradle-tooling-api-4.3.1.jar
/usr/share/gradle/lib/gradle-wrapper-4.3.1.jar
/usr/share/gradle/lib/groovy-all-2.4.12.jar
/usr/share/gradle/lib/guava-jdk5-17.0.jar
/usr/share/gradle/lib/jansi-1.14.jar
/usr/share/gradle/lib/javax.inject-1.jar
/usr/share/gradle/lib/jcip-annotations-1.0.jar
/usr/share/gradle/lib/jcl-over-slf4j-1.7.10.jar
/usr/share/gradle/lib/jsr305-1.3.9.jar
/usr/share/gradle/lib/jul-to-slf4j-1.7.10.jar
/usr/share/gradle/lib/kotlin-compiler-embeddable-1.1.51.jar
/usr/share/gradle/lib/kotlin-reflect-1.1.51.jar
/usr/share/gradle/lib/kotlin-sam-with-receiver-compiler-plugin-1.1.51.jar
/usr/share/gradle/lib/kotlin-stdlib-1.1.51.jar
/usr/share/gradle/lib/kryo-2.20.jar
/usr/share/gradle/lib/log4j-over-slf4j-1.7.10.jar
/usr/share/gradle/lib/minlog-1.2.jar
/usr/share/gradle/lib/native-platform-0.14.jar
/usr/share/gradle/lib/native-platform-freebsd-amd64-libcpp-0.14.jar
/usr/share/gradle/lib/native-platform-freebsd-amd64-libstdcpp-0.14.jar
/usr/share/gradle/lib/native-platform-freebsd-i386-libcpp-0.14.jar
/usr/share/gradle/lib/native-platform-freebsd-i386-libstdcpp-0.14.jar
/usr/share/gradle/lib/native-platform-linux-amd64-0.14.jar
/usr/share/gradle/lib/native-platform-linux-amd64-ncurses5-0.14.jar
/usr/share/gradle/lib/native-platform-linux-amd64-ncurses6-0.14.jar
/usr/share/gradle/lib/native-platform-linux-i386-0.14.jar
/usr/share/gradle/lib/native-platform-linux-i386-ncurses5-0.14.jar
/usr/share/gradle/lib/native-platform-linux-i386-ncurses6-0.14.jar
/usr/share/gradle/lib/native-platform-osx-amd64-0.14.jar
/usr/share/gradle/lib/native-platform-osx-i386-0.14.jar
/usr/share/gradle/lib/native-platform-windows-amd64-0.14.jar
/usr/share/gradle/lib/native-platform-windows-i386-0.14.jar
/usr/share/gradle/lib/objenesis-1.2.jar
/usr/share/gradle/lib/plugins/aether-api-1.13.1.jar
/usr/share/gradle/lib/plugins/aether-connector-wagon-1.13.1.jar
/usr/share/gradle/lib/plugins/aether-impl-1.13.1.jar
/usr/share/gradle/lib/plugins/aether-spi-1.13.1.jar
/usr/share/gradle/lib/plugins/aether-util-1.13.1.jar
/usr/share/gradle/lib/plugins/aws-java-sdk-core-1.11.6.jar
/usr/share/gradle/lib/plugins/aws-java-sdk-kms-1.11.6.jar
/usr/share/gradle/lib/plugins/aws-java-sdk-s3-1.11.6.jar
/usr/share/gradle/lib/plugins/bcpg-jdk15on-1.57.jar
/usr/share/gradle/lib/plugins/bcprov-jdk15on-1.57.jar
/usr/share/gradle/lib/plugins/biz.aQute.bndlib-3.4.0.jar
/usr/share/gradle/lib/plugins/bsh-2.0b4.jar
/usr/share/gradle/lib/plugins/commons-cli-1.2.jar
/usr/share/gradle/lib/plugins/commons-codec-1.6.jar
/usr/share/gradle/lib/plugins/dd-plist-1.20.jar
/usr/share/gradle/lib/plugins/google-api-client-1.22.0.jar
/usr/share/gradle/lib/plugins/google-api-services-storage-v1-rev78-1.22.0.jar
/usr/share/gradle/lib/plugins/google-http-client-1.22.0.jar
/usr/share/gradle/lib/plugins/google-http-client-jackson2-1.22.0.jar
/usr/share/gradle/lib/plugins/google-oauth-client-1.22.0.jar
/usr/share/gradle/lib/plugins/gradle-announce-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-antlr-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-build-cache-http-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-build-comparison-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-build-init-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-code-quality-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-composite-builds-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-dependency-management-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-diagnostics-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-ear-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-ide-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-ide-native-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-ide-play-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-ivy-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-jacoco-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-javascript-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-language-groovy-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-language-java-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-language-jvm-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-language-native-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-language-scala-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-maven-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-osgi-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-platform-base-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-platform-jvm-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-platform-native-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-platform-play-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-plugin-development-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-plugin-use-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-plugins-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-publish-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-reporting-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-resources-gcs-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-resources-http-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-resources-s3-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-resources-sftp-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-scala-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-signing-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-test-kit-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-testing-base-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-testing-jvm-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-testing-native-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-tooling-api-builders-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-version-control-4.3.1.jar
/usr/share/gradle/lib/plugins/gradle-workers-4.3.1.jar
/usr/share/gradle/lib/plugins/gson-2.7.jar
/usr/share/gradle/lib/plugins/hamcrest-core-1.3.jar
/usr/share/gradle/lib/plugins/httpclient-4.4.1.jar
/usr/share/gradle/lib/plugins/httpcore-4.4.4.jar
/usr/share/gradle/lib/plugins/ivy-2.2.0.jar
/usr/share/gradle/lib/plugins/jackson-annotations-2.6.6.jar
/usr/share/gradle/lib/plugins/jackson-core-2.6.6.jar
/usr/share/gradle/lib/plugins/jackson-databind-2.6.6.jar
/usr/share/gradle/lib/plugins/jatl-0.2.2.jar
/usr/share/gradle/lib/plugins/jcifs-1.3.17.jar
/usr/share/gradle/lib/plugins/jcommander-1.12.jar
/usr/share/gradle/lib/plugins/joda-time-2.8.2.jar
/usr/share/gradle/lib/plugins/jsch-0.1.54.jar
/usr/share/gradle/lib/plugins/junit-4.12.jar
/usr/share/gradle/lib/plugins/maven-aether-provider-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-artifact-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-compat-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-core-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-model-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-model-builder-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-plugin-api-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-repository-metadata-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-settings-3.0.4.jar
/usr/share/gradle/lib/plugins/maven-settings-builder-3.0.4.jar
/usr/share/gradle/lib/plugins/nekohtml-1.9.14.jar
/usr/share/gradle/lib/plugins/plexus-cipher-1.7.jar
/usr/share/gradle/lib/plugins/plexus-classworlds-2.4.jar
/usr/share/gradle/lib/plugins/plexus-component-annotations-1.5.5.jar
/usr/share/gradle/lib/plugins/plexus-container-default-1.5.5.jar
/usr/share/gradle/lib/plugins/plexus-interpolation-1.14.jar
/usr/share/gradle/lib/plugins/plexus-sec-dispatcher-1.3.jar
/usr/share/gradle/lib/plugins/plexus-utils-2.0.6.jar
/usr/share/gradle/lib/plugins/pmaven-common-0.8-20100325.jar
/usr/share/gradle/lib/plugins/pmaven-groovy-0.8-20100325.jar
/usr/share/gradle/lib/plugins/rhino-1.7R3.jar
/usr/share/gradle/lib/plugins/simple-4.1.21.jar
/usr/share/gradle/lib/plugins/snakeyaml-1.6.jar
/usr/share/gradle/lib/plugins/testng-6.3.1.jar
/usr/share/gradle/lib/plugins/wagon-file-2.4.jar
/usr/share/gradle/lib/plugins/wagon-http-2.4.jar
/usr/share/gradle/lib/plugins/wagon-http-shared4-2.4.jar
/usr/share/gradle/lib/plugins/wagon-provider-api-2.4.jar
/usr/share/gradle/lib/plugins/xbean-reflect-3.4.jar
/usr/share/gradle/lib/plugins/xercesImpl-2.9.1.jar
/usr/share/gradle/lib/plugins/xml-apis-1.3.04.jar
/usr/share/gradle/lib/reflectasm-1.07-shaded.jar
/usr/share/gradle/lib/slf4j-api-1.7.10.jar
/usr/share/gradle/media/gradle-icon-128x128.png
/usr/share/gradle/media/gradle-icon-16x16.png
/usr/share/gradle/media/gradle-icon-24x24.png
/usr/share/gradle/media/gradle-icon-256x256.png
/usr/share/gradle/media/gradle-icon-32x32.png
/usr/share/gradle/media/gradle-icon-48x48.png
/usr/share/gradle/media/gradle-icon-512x512.png
/usr/share/gradle/media/gradle-icon-64x64.png
/usr/share/gradle/media/gradle.icns

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gradle/LICENSE
/usr/share/package-licenses/gradle/subprojects_distributions_src_toplevel_NOTICE
/usr/share/package-licenses/gradle/subprojects_docs_src_docs_userguide_licenses.adoc
/usr/share/package-licenses/gradle/subprojects_docs_src_samples_application_src_dist_LICENSE
/usr/share/package-licenses/gradle/subprojects_docs_src_samples_play_custom-assets_copyright.txt
/usr/share/package-licenses/gradle/subprojects_docs_src_samples_play_custom-distribution_LICENSE
