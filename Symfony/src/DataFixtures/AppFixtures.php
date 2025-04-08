<?php

namespace App\DataFixtures;

use App\Entity\Category;
use App\Entity\Customer;
use App\Entity\Product;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Persistence\ObjectManager;

class AppFixtures extends Fixture
{
    public function load(ObjectManager $manager): void
    {
        $categories = [];

        for ($i = 1; $i <= 5; $i++) {
            $category = new Category();
            $category->setName('category ' . $i);
            $manager->persist($category);

            $categories[] = $category;
        }

        for ($i = 1; $i <= 20; $i++) {
            $randomCategory = $categories[array_rand($categories)];

            $product = new Product();
            $product->setName('product '.$i);
            $product->setPrice(mt_rand(10, 100));
            $product->setQuantity(mt_rand(0, 1000));
            $product->setCategory($randomCategory);
            $manager->persist($product);
        }


        for ($i = 1; $i <= 5; $i++) {
            $customer = new Customer();
            $customer->setFirstName("John");
            $customer->setLastName("Doe");
            $customer->setEmail("customer$i@email.com");
            $manager->persist($customer);
        }

        $manager->flush();
    }
}
