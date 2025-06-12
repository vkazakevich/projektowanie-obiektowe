package models

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPaymentModel(t *testing.T) {
	db := setupTestDB()

	t.Run("It creates Payment", func(t *testing.T) {
		p := &Payment{Amount: 9999, IsPaid: true}
		result := db.Create(&p)

		assert.NoError(t, result.Error)
		assert.Equal(t, int64(1), result.RowsAffected)
		assert.NotNil(t, p.ID)
	})

	t.Run("It can't creates Payment if zero amount", func(t *testing.T) {
		p := &Payment{Amount: 0, IsPaid: false}
		result := db.Create(&p)

		assert.Error(t, result.Error)
		assert.Equal(t, int64(0), result.RowsAffected)

		assert.Equal(t, uint(0), p.ID)
		assert.Equal(t, uint(0), p.Amount)
		assert.Equal(t, false, p.IsPaid)
	})
}
