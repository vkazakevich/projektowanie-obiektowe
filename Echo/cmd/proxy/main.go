package main

import (
	"github.com/labstack/echo/v4"
	"github.com/vkazakevich/projektowanie-obiektowe/Echo/internal/app/db"
	"github.com/vkazakevich/projektowanie-obiektowe/Echo/internal/app/handlers"
	"github.com/vkazakevich/projektowanie-obiektowe/Echo/internal/app/utils"
)

func main() {

	db := db.InitDatabase()
	utils.FillDBSeeds(db)

	e := echo.New()

	h := &handlers.Handler{DB: db}

	w := e.Group("/weather")
	w.GET("/:city", h.GetTheWeatherByCity)
	w.GET("", h.GetTheWeatherByCities)

	e.Logger.Fatal(e.Start(":8000"))
}
