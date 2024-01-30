#include <stdlib.h>
int main()
{
system("sudo waydroid session stop");
system("sudo waydroid init -s GAPPS -f");
system("waydroid show-full-ui");
}
