import subprocess
import re
from versions.package import Package
from versions.pypi import version_pypi
from versions.alpine import version_alpine
from versions.debian import version_debian
from versions.docker import get_docker_tags

class Dockerfile:
    def __init__(self, config, filepath):
        self.changed =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 False
        self.config =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 config
        self.filepath =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 filepath
        self.filepathmin =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 filepath.replace(config.rootdir, "")


    def commit(self, package, installed, available):
        subprocess.run(["git", "add", self.filepath])
        msg =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 self.config.commit_msg
        msg =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 msg.replace("[package]", package)
        msg =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 msg.replace("[from_version]", installed)
        msg =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 msg.replace("[to_version]", available)
        subprocess.run(["git", "commit", "-m", msg])
        with open(f"{self.config.rootdir}/changes", "a") as changes:
            changes.write(f"- {msg}\n")
        self.changed =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 True


    def get_content(self):
        with open(self.filepath, "r") as f:
            content =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 f.read()
        return content


    def write_content(self, content):
        with open(self.filepath, "w") as f:
            f.write(content)


    def update(self):
        print(f"Checking for updates in '{self.filepathmin}'")
        content =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 self.get_content()
        if "RUN" not in content:
            return

        if "base" not in self.config.exclude_type:
            self.update_base_image(content)
        if "pip" not in self.config.exclude_type:
            self.update_pip_packages(content)
        if "apk" not in self.config.exclude_type:
            self.update_alpine_packages(content)
        #if "apt" not in self.config.exclude_type:
        #    self.update_debian_packages(content)

        return self.changed


    def get_packages(self, content):
        packages =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 []
        tmp =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 content.split("RUN ")[1]
        tmp =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 [x for x in tmp.split("\n") if "=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0" in x]
        for pkg in tmp:
            packages.extend([x for x in pkg.split(" ") if "=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0" in x])
        return packages


    def update_base_image(self, content):
        installed =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 content.split("FROM ")[1].split("\n")[0].strip()
        available =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 None
        image =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 None
        if ":" not in installed:
            return
        if "alpine" in installed:
            image =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 "alpine"
            if len(installed.split(":")[-1].split(".")) !=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 3:
                return
            for tag in get_docker_tags(image):
                if len(tag["name"].split(".")) =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 3:
                    available =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 f"alpine:{tag['name']}"
                    break

        if "debian" in installed:
            image =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 "debian"
            if len(installed.split(":")[-1].split(".")) !=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 2:
                return
            for tag in sorted(get_docker_tags(image), reverse=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0True):
                if "-slim" in installed:
                    if len(tag.split(".")) =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 2 and "-slim" in tag and int(tag.split(".")[0]) >=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 10:
                        available =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 f"debian:{tag}"
                        break
                else:
                    if len(tag.split(".")) =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 2 and "-slim" not in tag and int(tag.split(".")[0]) >=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 10:
                        available =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 f"debian:{tag}"
                        break

        if available is not None and image is not None:
            if available !=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 installed:
                content =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 content.replace(installed, available)
                self.write_content(content)
                self.commit(image, installed.split(":")[-1], available.split(":")[-1])


    def update_pip_packages(self, content):
        if re.search(r'pip(|3)\ install', content) is None:
            return

        for pkg in self.get_packages(content):
            package =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 Package(pkg, "=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0")
            if package.name in self.config.exclude_package:
                continue
            package.available =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 version_pypi(package.name)
            if package.updated:
                content =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 self.get_content()
                content =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 content.replace(package.old, package.new)
                self.write_content(content)
                self.commit(package.name, package.installed, package.available)


    def update_alpine_packages(self, content):
        if re.search(r'apk add', content) is None:
            return

        for pkg in self.get_packages(content):
            if "=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0" not in pkg:
                package =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 Package(pkg)
                package.available =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 version_alpine(package.name)
                if package.updated:
                    content =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 self.get_content()
                    content =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 content.replace(package.old, package.new)
                    self.write_content(content)
                    self.commit(package.name, package.installed, package.available)


    def update_debian_packages(self, content):
        if re.search(r'apt(|-get)\ install', content) is None:
            return

        for pkg in self.get_packages(content):
            if "=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0=3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0" not in pkg:
                package =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 Package(pkg)
                package.available =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 version_debian(package.name)
                if package.updated:
                    content =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 self.get_content()
                    content =3.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r03.6.6-r0 content.replace(package.old, package.new)
                    self.write_content(content)
                    self.commit(package.name, package.installed, package.available)