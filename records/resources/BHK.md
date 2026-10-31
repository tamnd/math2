---
records:
    - id: BHK11YYQ2S
      kind: monograph
      title: An Introduction to Laplace Transforms and Fourier Series
      creators:
        - name: Philip P. G. Dyke
          role: author
      date: "2001"
      expressions:
        - key: e1
          kind: edition
          date: "2001"
          ids:
            doi:
                - 10.1007/978-1-4471-0505-3
                - 10.1007/978-1-4471-6395-4
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2001"
              ids:
                isbn:
                    - "9781852330156"
                    - "9781447105053"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer London
              date: "2014"
              ids:
                isbn:
                    - "9781447163947"
                    - "9781447163954"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-0505-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-6395-4
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: BHKT0ZGR7J
      kind: edited-volume
      title: Recent Trends in Orthogonal Polynomials and Approximation Theory
      creators:
        - name: Jorge Arvesú
          role: editor
        - name: Francisco Marcellán
          role: editor
        - name: Andrei Martínez-Finkelshtein
          role: editor
      date: "2010"
      msc:
        - code: 33-06
          from: zbmath_search
        - code: 33C47
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2010"
          ids:
            doi: 10.1090/conm/507
            zbl: "1182.33001"
            zbl_id: "5679264"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2010"
              ids:
                isbn:
                    - "9780821848036"
                    - "9780821858332"
                    - "9780821881866"
              access:
                class: record
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/507
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "5679264"
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
