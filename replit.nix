{ pkgs }: {
	deps = [
		pkgs.jupyter
        pkgs.jq
        pkgs.python3
        pkgs.python3Packages.pip
        pkgs.python3Packages.pandas
        pkgs.python3Packages.numpy
    pkgs.cowsay
	];
}