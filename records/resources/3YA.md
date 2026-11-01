---
records:
    - id: 3YA72PMNQT
      kind: monograph
      title: Rational Points on Elliptic Curves
      creators:
        - name: Joseph H. Silverman
          role: author
        - name: John Tate
          role: author
      date: "1992"
      msc:
        - code: 11G05
          from: zbmath_search
        - code: 11-01
          from: zbmath_search
        - code: 14-01
          from: zbmath_search
        - code: 11G15
          from: zbmath_search
        - code: 11D25
          from: zbmath_search
        - code: 14G05
          from: zbmath_search
        - code: 14G15
          from: zbmath_search
        - code: 14H52
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1992"
          ids:
            doi:
                - 10.1007/978-1-4757-4252-7
                - 10.1007/978-3-319-18588-0
            zbl: "0752.14034"
            zbl_id: "53994"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1992"
              ids:
                isbn:
                    - "9781441931016"
                    - "9781475742527"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2015"
              ids:
                isbn:
                    - "9783319185873"
                    - "9783319185880"
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
          native_id: 10.1007/978-1-4757-4252-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-18588-0
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "53994"
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
