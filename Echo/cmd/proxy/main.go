package main

import (
	"github.com/labstack/echo/v4"
	"github.com/vkazakevich/projektowanie-obiektowe/Echo/internal/app/handlers"
)

func main() {
	e := echo.New()

	h := &handlers.Handler{}

	w := e.Group("/weather")
	w.GET("/:city", h.GetTheWeatherByCity)

	e.Logger.Fatal(e.Start(":8000"))
}
