{ pkgs }: {
    deps = [
      pkgs.python39Packages.django
      pkgs.nodePackages.vscode-langservers-extracted
      pkgs.nodePackages.typescript-language-server
    ];
  }