---
records:
    - id: BPT0F80EQW
      kind: monograph
      title: Numerical Approximation of Hyperbolic Systems of Conservation Laws
      creators:
        - name: Edwige Godlewski
          role: author
        - name: Pierre-Arnaud Raviart
          role: author
      date: "1996"
      msc:
        - code: 65M06
          from: zbmath_search
        - code: 35L65
          from: zbmath_search
        - code: 76M20
          from: zbmath_search
        - code: 76N15
          from: zbmath_search
        - code: 65-02
          from: zbmath_search
        - code: 35-02
          from: zbmath_search
        - code: 76-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1996"
          ids:
            doi:
                - 10.1007/978-1-0716-1344-3
                - 10.1007/978-1-4612-0713-9
            zbl: "0860.65075"
            zbl_id: "954087"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2021"
              ids:
                isbn:
                    - "9781071613429"
                    - "9781071613443"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1996"
              ids:
                isbn:
                    - "9781461268789"
                    - "9781461207139"
              access:
                class: record
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-0716-1344-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0713-9
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "954087"
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
