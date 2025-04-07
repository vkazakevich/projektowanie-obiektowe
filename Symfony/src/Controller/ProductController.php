<?php

namespace App\Controller;

use App\Dto\ProductDto;
use App\Entity\Product;
use App\Repository\ProductRepository;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\HttpKernel\Attribute\MapRequestPayload;

#[Route('/products')]
final class ProductController extends AbstractController
{
    #[Route(name: 'api_product', methods: ['GET'])]
    public function index(ProductRepository $productRepository): JsonResponse
    {
        return $this->json($productRepository->findAll());
    }

    #[Route(name: 'app_product_create', methods: ['POST'])]
    public function create(
        #[MapRequestPayload] ProductDto $productDto, 
        ProductRepository $productRepository
    ): JsonResponse
    {
        $product = new Product();

        $product->setName($productDto->name);
        $product->setPrice($productDto->price);
        $product->setQuantity($productDto->quantity);
        $product->setDescription($productDto->description);

        $productRepository->save($product, true);

        return $this->json($product, Response::HTTP_CREATED);
    }

    #[Route('/{id}', name: 'app_product_show', methods: ['GET'])]
    public function show(Product $product): JsonResponse
    {
        return $this->json($product);
    }

    #[Route('/{id}', name: 'app_product_update', methods: ['PUT'])]
    public function update(
        #[MapRequestPayload] ProductDto $productDto, 
        Product $product,
        ProductRepository $productRepository
    ): JsonResponse
    {
        $product->setName($productDto->name);
        $product->setPrice($productDto->price);
        $product->setQuantity($productDto->quantity);
        $product->setDescription($productDto->description);

        $productRepository->save($product, true);

        return $this->json($product);
    }

    #[Route('/{id}', name: 'app_product_delete', methods: ['DELETE'])]
    public function delete(Product $product, ProductRepository $productRepository): JsonResponse
    {
        $productRepository->remove($product, true);

        return $this->json('', Response::HTTP_NO_CONTENT);
    }
}
