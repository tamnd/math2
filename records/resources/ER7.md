---
records:
    - id: ER754MFW11
      kind: monograph
      title: Introduction to Knot Theory
      creators:
        - name: Richard H. Crowell
          role: author
        - name: Ralph H. Fox
          role: author
      date: "1977"
      msc:
        - code: 20F34
          from: zbmath_search
        - code: 57M05
          from: zbmath_search
        - code: 57M30
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          label: 4th edition
          language: en
          date: "1977"
          ids:
            doi: 10.1007/978-1-4612-9935-6
            zbl: "0362.55001"
            zbl_id: "3563912"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1977"
              ids:
                isbn:
                    - "9781461299370"
                    - "9781461299356"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-9935-6
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3563912"
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
---
