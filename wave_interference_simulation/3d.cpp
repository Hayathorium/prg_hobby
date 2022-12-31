#include "screen.h"
#include <cstdlib>
using namespace std;

int main()
{
    Screen screen;

    for(int i=0; i< 100; i++)
    {
        screen.pixel(static_cast<float>(rand()%640), static_cast<float>(rand()%480));
    }

    while(true)
    {
        screen.show();
        screen.input();
        screen.input();
    }
    return 0;
}
