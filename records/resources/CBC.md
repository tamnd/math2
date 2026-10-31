---
records:
    - id: CBCCH5VTMQ
      kind: preprint
      title: Point Configurations in Brownian Traces
      creators:
        - name: P. Kosenko
          role: author
        - name: J. M. Medina
          role: author
        - name: A. Yavicoli
          role: author
      date: "2026-10-02"
      subjects:
        - system: arxiv
          code: math.PR
        - system: arxiv
          code: math.CA
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-02"
          ids:
            arxiv: "2610.04000"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.04000"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
    - id: CBCD1FX8KX
      kind: monograph
      title: 'Geometric Analysis: Cetraro, Italy 2018'
      creators:
        - name: Ailana Fraser
          role: author
          ids:
            orcid: 0000-0003-3596-9260
        - name: André Neves
          role: author
        - name: Peter M. Topping
          role: author
          ids:
            orcid: 0000-0002-7346-7643
        - name: Paul C. Yang
          role: author
        - name: Matthew J. Gursky
          role: editor
          ids:
            orcid: 0000-0002-6868-3173
        - name: Andrea Malchiodi
          role: editor
          ids:
            orcid: 0000-0001-5029-122X
      date: "2020"
      expressions:
        - key: e1
          kind: edition
          date: "2020"
          ids:
            doi: 10.1007/978-3-030-53725-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2020"
              ids:
                isbn:
                    - "9783030537241"
                    - "9783030537258"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-53725-8
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
