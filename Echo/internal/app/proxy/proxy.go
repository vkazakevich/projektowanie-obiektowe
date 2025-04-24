package proxy

import (
	"encoding/json"
	"io"
	"net/http"
)

type ApiWeatherData struct {
	Temperature string `json:"temperatura"`
	Data        string `json:"data_pomiaru"`
	Time        string `json:"godzina_pomiaru"`
}

func FetchTheWeatherByCity(city string) (*ApiWeatherData, error) {
	response, err := http.Get("https://danepubliczne.imgw.pl/api/data/synop/station/" + city)

	if err != nil {
		return nil, err
	}

	responseData, err := io.ReadAll(response.Body)
	if err != nil {
		return nil, err
	}

	var responseObject ApiWeatherData
	json.Unmarshal(responseData, &responseObject)

	return &responseObject, nil
}
