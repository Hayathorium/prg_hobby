#include <include/SDL.h>
#include <vector>
#include <iostream>
using namespace std;
//#define PI 3.14159265358979323846264338327950288

class Screen
{
    SDL_Event e;
    SDL_Window* window;
    SDL_Renderer* renderer;
    vector<SDL_FPoint> points;
    SDL_FPoint p;

    public:

    Screen()
    {
        SDL_Init(SDL_INIT_VIDEO);
        SDL_CreateWindowAndRenderer(640*2, 480*2, 0, &window, &renderer);
        SDL_RenderSetScale(renderer, 2, 2);
    }

    void pixel(float x, float y)
    {
        p = {x,y};
        points.push_back(p);
    }

    void show()
    {
        SDL_SetRenderDrawColor(renderer,0,0,0,255);
        SDL_RenderClear(renderer);

        SDL_SetRenderDrawColor(renderer,255,255,255,255);
        for(auto& point : points)
        {
            SDL_RenderDrawPointF(renderer, point.x, point.y);
            //cout << point.x << endl;
        }

        SDL_RenderPresent(renderer);
    }

    void input()
    {
        while(SDL_PollEvent(&e))
        {
            if(e.type == SDL_QUIT)
            {
                SDL_Quit();
                exit(0);
            }
        }
    }
};
