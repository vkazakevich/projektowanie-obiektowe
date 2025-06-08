package models

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCustomerModel(t *testing.T) {
	db := setupTestDB()

	t.Run("It creates Customer", func(t *testing.T) {
		p := &Customer{FirstName: "Test Name", LastName: "Test Last Name", Email: "test@test.com"}
		result := db.Create(&p)

		assert.NoError(t, result.Error)
		assert.Equal(t, int64(1), result.RowsAffected)

		assert.NotNil(t, p.ID)
		assert.Equal(t, "Test Name", p.FirstName)
		assert.Equal(t, "Test Last Name", p.LastName)
		assert.Equal(t, "test@test.com", p.Email)
	})

	t.Run("It can't creates Customer if empty", func(t *testing.T) {
		c := &Customer{FirstName: "", LastName: "", Email: ""}
		result := db.Create(&c)

		assert.Error(t, result.Error)
		assert.Equal(t, int64(0), result.RowsAffected)

		assert.Equal(t, uint(0), c.ID)
		assert.Equal(t, "", c.FirstName)
		assert.Equal(t, "", c.LastName)
		assert.Equal(t, "", c.Email)
	})
}
