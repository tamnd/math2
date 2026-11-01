---
records:
    - id: AQG12GJ7CV
      kind: monograph
      title: An Introduction to Complex Function Theory
      creators:
        - name: Bruce P. Palka
          role: author
      date: "1991"
      msc:
        - code: 30-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1991"
          ids:
            doi: 10.1007/978-1-4612-0975-1
            zbl: "0726.30001"
            zbl_id: "48731"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1991"
              ids:
                isbn:
                    - "9781461269670"
                    - "9781461209751"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0975-1
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "48731"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: AQGEM4XAKD
      kind: preprint
      title: Deforming Calabi-Yau Threefolds
      creators:
        - name: Mark Gross
          role: author
      date: "1995-06-26"
      subjects:
        - system: arxiv
          code: alg-geom
        - system: arxiv
          code: math.AG
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "1995-06-26"
          ids:
            arxiv: alg-geom/9506022
            doi: 10.1007/s002080050072
      scope:
        value: out
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: alg-geom/9506022
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to out
---
