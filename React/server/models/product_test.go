package models

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

const PRODUCT_NAME = "Test Product"

func TestProductModel(t *testing.T) {
	db := setupTestDB()

	t.Run("It creates Product", func(t *testing.T) {
		p := &Product{Name: PRODUCT_NAME, Quantity: 10, Price: 10}
		result := db.Create(&p)

		assert.NoError(t, result.Error)
		assert.Equal(t, int64(1), result.RowsAffected)
		assert.NotNil(t, p.ID)
	})

	t.Run("It can't creates Product if empty name", func(t *testing.T) {
		p := &Product{Name: ""}
		result := db.Create(&p)

		assert.Error(t, result.Error)
		assert.Equal(t, int64(0), result.RowsAffected)

		assert.Equal(t, uint(0), p.ID)
		assert.Equal(t, "", p.Name)
	})

	t.Run("It updates Product", func(t *testing.T) {
		p := &Product{Name: PRODUCT_NAME}
		db.Create(&p)

		p.Name = "Updated Test Product"
		p.Price = 9999
		p.Quantity = 9999
		result := db.Save(p)

		assert.NoError(t, result.Error)
		assert.Equal(t, int64(1), result.RowsAffected)

		assert.Equal(t, "Updated Test Product", p.Name)
		assert.Equal(t, uint(9999), p.Price)
		assert.Equal(t, uint(9999), p.Quantity)
	})

	t.Run("It can't updates Product with empty name", func(t *testing.T) {
		p := &Product{Name: PRODUCT_NAME}
		db.Create(&p)

		p.Name = ""
		result := db.Save(p)

		assert.Error(t, result.Error)
		assert.Equal(t, int64(0), result.RowsAffected)

		assert.Equal(t, "", p.Name)
	})

	t.Run("It shows Product", func(t *testing.T) {
		newProduct := &Product{
			Name:     PRODUCT_NAME,
			Price:    9999,
			Quantity: 9999,
		}
		db.Create(&newProduct)

		var p Product
		result := db.Last(&p)

		assert.NoError(t, result.Error)
		assert.Equal(t, int64(1), result.RowsAffected)

		assert.Equal(t, PRODUCT_NAME, p.Name)
		assert.Equal(t, uint(9999), p.Price)
		assert.Equal(t, uint(9999), p.Quantity)
	})

	t.Run("It deletes Product", func(t *testing.T) {
		p := &Product{
			Name:     PRODUCT_NAME,
			Price:    9999,
			Quantity: 9999,
		}
		db.Create(&p)

		result := db.Delete(&Product{}, p.ID)

		assert.NoError(t, result.Error)
		assert.Equal(t, int64(1), result.RowsAffected)
	})
}
